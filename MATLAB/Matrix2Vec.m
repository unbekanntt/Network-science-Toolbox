function dFCstream_2D = Matrix2Vec(dFCstream_3D)

% FUNCTION dFCstream_2D = Matrix2Vec(dFCstream_3D)
% takes '3D' dFCstream as input and convert it to '2D' dFCstream
%
% Reference: Lucas Arbabyazd et al. (2020) MethodsX

if (ndims(dFCstream_3D) == 2)
    disp('You do not need this function since your dFCstream is alread 2D')
    return
end

n = size(dFCstream_3D, 1);
l = n*(n-1)/2;
F = size(dFCstream_3D, 3);
xo = find(tril(ones(n),-1));

dFCstream_2D = zeros(l, F);

for f = 1:F
    fc = dFCstream_3D(:,:,f);
    dFCstream_2D(:,f) = fc(xo);
end

